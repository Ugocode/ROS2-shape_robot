from setuptools import setup

package_name = 'my_robot_controller3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    # packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ugoboss',
    maintainer_email='ugoboss@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller3.my_first_node:main",
            "draw_circle = my_robot_controller3.draw_circle:main",
            "draw_square = my_robot_controller3.draw_square:main",
            "draw_pentagon = my_robot_controller3.draw_pentagon:main",
            "draw_triangle = my_robot_controller3.draw_triangle:main",
            "draw_hexagon = my_robot_controller3.draw_hexagon:main",
            "draw_rectangle = my_robot_controller3.draw_rectangle:main",
        ],
    },
)
