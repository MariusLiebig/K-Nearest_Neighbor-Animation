from manim import *

class IntroductoryScene(Scene):
    def construct(self):
        # Title Scene
        title = Text("K-Nearest Neighbor (KNN)", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))




class KNNExplained(Scene):
    def construct(self):
        # Visualize KNN Working
        points = [
            Dot(point=[-3, 1.2, 0], color=RED),
            Dot(point=[-2, 2, 0], color=RED),
            Dot(point=[-2, 1, 0], color=RED),
            Dot(point=[-1.9, 0.87, 0], color=RED),
            Dot(point=[-1.8, 1.2, 0], color=RED),

            Dot(point=[1, -1.5, 0], color=GREEN),
            Dot(point=[0.5, -1, 0], color=GREEN),
            Dot(point=[0.2, -0.8, 0], color=GREEN),
            Dot(point=[0.8, -0.9, 0], color=GREEN),
            Dot(point=[-0.2, -2, 0], color=GREEN),

            Dot(point=[1, 1.5, 0], color=BLUE),
            Dot(point=[1.5, 1, 0], color=BLUE),
            Dot(point=[0.9, 0.7, 0], color=BLUE),
            Dot(point=[1.8, 0.9, 0], color=BLUE),
            Dot(point=[2, 2, 0], color=BLUE),
        ]

        # Test point and radius
        test_point_coords = [0, 0, 0]
        radius = 1.3

        #Initialize axis 
        x_axis = NumberLine(
            x_range=[0, 256, 256],  
            length=10,  
            color=WHITE,
            include_numbers=False,
            label_direction=DOWN  
        ) 

        y_axis = NumberLine(
            x_range=[0, 256, 256],  
            length=7,  
            color=WHITE,
            include_numbers=False,
            label_direction=LEFT,  
            rotation=PI / 2  
        )  

        x_axis.add_tip(tip_length=0.2)
        y_axis.add_tip(tip_length=0.2)

        x_axis.shift(3.1 * DOWN )
        y_axis.shift(4 * LEFT)
       
        x_label = Text("Andre Piksel", font_size=24).next_to(x_axis, DOWN, buff=0.3)
        y_label = Text("Første Piksel", font_size=24).next_to(y_axis, LEFT,  buff=0.4)

        # Add axes to the scene
        self.play(Create(x_axis), Create(y_axis))
        self.play(Write(x_label), Write(y_label))


        # Display all points
        self.play(*[FadeIn(dot) for dot in points if dot.get_color() == RED])

        self.play(*[FadeIn(dot) for dot in points if dot.get_color() == BLUE])

        self.play(*[FadeIn(dot) for dot in points if dot.get_color() == GREEN])

        self.wait(1)

        # Show the test point
        test_point = Dot(point=[0, 0, 0], color=WHITE).scale(1.5)
        self.play(FadeIn(test_point))
        self.wait(1)


        #Draw the lines
        lines = []
        for point in points:
            line = Line(test_point.get_center(), point.get_center(), color=YELLOW)
            lines.append(line)
            self.play(Create(line), run_time=0.2)

        self.play(*[FadeOut(line) for line in lines], run_time=1.5)

        # Draw the circle
        neighbors_circle = Circle(radius=radius, color=YELLOW).move_to(test_point)
        self.play(Create(neighbors_circle))
        self.wait(0.5)

        # Highlight points within the circle

        labels_red = []
        labels_green = []
        labels_blue = []

        for i, dot in enumerate(points):
            distance = ((dot.get_center()[0] - test_point_coords[0])**2 + 
                        (dot.get_center()[1] - test_point_coords[1])**2)**0.5
            color = dot.get_color()

            if distance <= radius:
                if color == RED:
                    label = Text(str(len(labels_red) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_red.append(label)
                    self.play(FadeIn(label), run_time=0.4)
                elif color == GREEN:
                    label = Text(str(len(labels_green) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_green.append(label)
                    self.play(FadeIn(label), run_time=0.4)
                elif color == BLUE:
                    label = Text(str(len(labels_blue) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_blue.append(label)
                    self.play(FadeIn(label), run_time=0.4)

        self.wait(0.5) 
        self.play(test_point.animate.set_color(GREEN))
        self.wait(2)

       
        


        self.wait(0.5)

        self.play(FadeOut(neighbors_circle, *points, *labels_red, *labels_green, *labels_blue, test_point, x_axis, y_axis, x_label, y_label))



class KNNExplained3D(ThreeDScene):
    def construct(self):
        # Initialize 
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Visualize KNN Working in 3D
        points = [
            Dot3D(point=[-3, 1.5, 1], color=RED),
            Dot3D(point=[-2, 2, -1], color=RED),
            Dot3D(point=[-2, 1, 0.5], color=RED),
            Dot3D(point=[-1.9, 0.87, -0.8], color=RED),
            Dot3D(point=[-1.8, 1.2, 0], color=RED),

            Dot3D(point=[1, -1.5, 0.5], color=GREEN),
            Dot3D(point=[0.5, -1, -1], color=GREEN),
            Dot3D(point=[0.2, -0.8, 0.7], color=GREEN),
            Dot3D(point=[0.8, -0.9, -0.5], color=GREEN),
            Dot3D(point=[-0.2, -2, 0], color=GREEN),

            Dot3D(point=[1, 1.5, -0.7], color=BLUE),
            Dot3D(point=[1.5, 1, 0.5], color=BLUE),
            Dot3D(point=[0.9, 0.7, -1.5], color=BLUE),
            Dot3D(point=[1.8, 0.9, 0.3], color=BLUE),
            Dot3D(point=[2, 2, -0.2], color=BLUE),
        ]

        test_point_coords = [0, 0, 0]
        radius = 1.5

        # Display all points
        self.play(*[FadeIn(dot) for dot in points])
        self.wait(1)

        test_point = Dot3D(point=test_point_coords, color=WHITE).scale(1.5)
        self.play(FadeIn(test_point))
        self.wait(1)

        # Draw the 3D sphere
        neighbors_sphere = Sphere(radius=radius, color=YELLOW, fill_opacity=0.2).move_to(test_point)
        self.play(Create(neighbors_sphere))
        self.wait(2)

        # Highlight points within the sphere
        labels_red = []
        labels_green = []
        labels_blue = []

        for i, dot in enumerate(points):
            distance = (
                (dot.get_center()[0] - test_point_coords[0]) ** 2
                + (dot.get_center()[1] - test_point_coords[1]) ** 2
                + (dot.get_center()[2] - test_point_coords[2]) ** 2
            ) ** 0.5
            color = dot.get_color()

            if distance <= radius:
                if color == RED:
                    label = Text(str(len(labels_red) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_red.append(label)
                    self.play(FadeIn(label))
                elif color == GREEN:
                    label = Text(str(len(labels_green) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_green.append(label)
                    self.play(FadeIn(label))
                elif color == BLUE:
                    label = Text(str(len(labels_blue) + 1), font_size=24, color=color).next_to(dot, UP)
                    labels_blue.append(label)
                    self.play(FadeIn(label))

        self.wait(2)

        self.play(test_point.animate.set_color(GREEN))
        self.wait(2)

        self.play(FadeOut(neighbors_sphere, *points, *labels_red, *labels_green, *labels_blue))
        self.stop_ambient_camera_rotation()

class MNISTDataset(Scene):
    def construct(self):
        

        # Dataset Visualization
        mnist_images = VGroup(
            *[Square().set_fill(WHITE, opacity=0.5) for _ in range(9)]
        ).arrange_in_grid(rows=3, cols=3, buff=0.2)

        mnist_labels = VGroup(
            *[Text(str(i), font_size=32) for i in range(9)]
        ).arrange_in_grid(rows=3, cols=3, buff=0.2)

        for img, label in zip(mnist_images, mnist_labels):
            label.move_to(img)

        self.play(FadeIn(mnist_images, shift=UP))
        self.play(Write(mnist_labels))
        self.wait(3)
        self.play(FadeOut(mnist_images, mnist_labels))

        

import random


class KNNVisualization(Scene):
    def construct(self):
        # Initial points with their colors
        points = [
            Dot(point=[-3, 1.2, 0], color=RED),
            Dot(point=[-2, 2, 0], color=RED),
            Dot(point=[-2, 1, 0], color=RED),
            Dot(point=[-1.9, 0.87, 0], color=RED),
            Dot(point=[-1.8, 1.2, 0], color=RED),

            Dot(point=[1, -1.5, 0], color=GREEN),
            Dot(point=[0.5, -1, 0], color=GREEN),
            Dot(point=[0.2, -0.8, 0], color=GREEN),
            Dot(point=[0.8, -0.9, 0], color=GREEN),
            Dot(point=[-0.2, -2, 0], color=GREEN),

            Dot(point=[1, 1.5, 0], color=BLUE),
            Dot(point=[1.5, 1, 0], color=BLUE),
            Dot(point=[0.9, 0.7, 0], color=BLUE),
            Dot(point=[1.8, 0.9, 0], color=BLUE),
            Dot(point=[2, 2, 0], color=BLUE),
        ]

        # Display initial points
        self.play(*[FadeIn(dot) for dot in points])
        self.wait(1)

        for _ in range(8):
            new_dot_coords = [
                random.uniform(-3, 3),  
                random.uniform(-2, 2),  
                0
            ]
            new_dot = Dot(point=new_dot_coords, color=WHITE)

            
            closest_distance = float("inf")
            self.play(FadeIn(new_dot))

            closest_color = WHITE
            for existing_dot in points:
                distance = np.linalg.norm(
                    np.array(new_dot_coords) - np.array(existing_dot.get_center())
                )
                if distance < closest_distance:
                    closest_distance = distance
                    closest_color = existing_dot.get_color()

            self.play(new_dot.animate.set_color(closest_color))

            self.wait(0.5)

            points.append(new_dot)
