from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """
    Generates the launch description to start the talker and listener nodes.
    """
    return LaunchDescription([
        Node(
            package='ros2_test',
            executable='talker',
            name='my_talker'
        ),
        Node(
            package='ros2_test',
            executable='listener',
            name='my_listener'
        )
    ])