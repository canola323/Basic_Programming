public class ShapeArray
{
    public static void main(String[] args)
    {
        // Create one object of each type
        Sphere sphere = new Sphere(3.0);
        Cylinder cylinder = new Cylinder(2.0, 5.0);
        Cone cone = new Cone(2.0, 4.0);

        // Store them in a Shape array
        Shape[] shapeArray = {sphere, cylinder, cone};

        // Print each object
        for (Shape shape : shapeArray)
        {
            System.out.println(shape);
        }
    }
}