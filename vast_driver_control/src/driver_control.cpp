#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int16MultiArray.h>
#include <Eigen/Dense>

using namespace Eigen;

#define L 0.1   // The length from center robot to each wheel (meter)
#define R 0.05  // The Wheel radius

geometry_msgs::Twist vel;

void velCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
    vel = *msg;
}

std_msgs::Int16MultiArray robotVel2PWM(const geometry_msgs::Twist& vel, const MatrixXf& inv_matrix)
{
    Matrix<float, 3, 1> robot_vel;
    Matrix<float, 4, 1> wheel_vel;

    robot_vel << vel.linear.x, vel.linear.y, vel.angular.z*L;
    wheel_vel = inv_matrix * robot_vel;

    float w1, w2, w3, w4;
    w1 = wheel_vel(0,0); w2 = wheel_vel(1,0);
    w3 = wheel_vel(2,0); w2 = wheel_vel(3,0);

    // Convert wheel velocity to pwm
    int pwm0, pwm1, pwm2, pwm3;
    // Code something ...

    // Load pwm values to output
    std_msgs::Int16MultiArray pwm;
    pwm.data.clear();
    pwm.data.push_back(pwm0);
    pwm.data.push_back(pwm1);
    pwm.data.push_back(pwm2);
    pwm.data.push_back(pwm3);
    return pwm;
}

int main(int argc, char** argv)
{
    // Init ROS node
    ros::init(argc, argv, "driver_control");
    ros::NodeHandle nh;
    
    // Publisher
    ros::Publisher pwm_pub = nh.advertise<std_msgs::Int16MultiArray>("/pwm", 100);

    // Subscriber
    ros::Subscriber vel_sub = nh.subscribe("/cmd_vel", 100, velCallback);

    // Declare the Forward and Inverse Kinematic Matrices
    MatrixXf fwd_matrix(3,4);
    MatrixXf inv_matrix(4,3); 
    fwd_matrix <<   -1/sqrt(2), -1/sqrt(2), 1/sqrt(2), 1/sqrt(2),
                    1/sqrt(2), -1/sqrt(2), -1/sqrt(2), 1/sqrt(2),
                    1, 1, 1, 1;
    inv_matrix = fwd_matrix.transpose() * (fwd_matrix*fwd_matrix.transpose()).inverse();

    ros::Rate r(100);
    while(ros::ok())
    {
        std_msgs::Int16MultiArray pwm = robotVel2PWM(vel, inv_matrix);
        pwm_pub.publish(pwm);

        r.sleep();
        ros::spinOnce();
    }
    return 0;
}