public class Cylinder extends Shape {
    private double radius;
    private double height;

    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    @Override
    public double surface_area() {
        return (2 * Math.PI * Math.pow(radius, 2)) * (2 * Math.PI * radius * height);
    }

    @Override
    public double volume() {
        return Math.PI * Math.pow(radius, 2) * height;
    }

    @Override
    public String toString() {
        return "Cylinder\n" + 
               "Radius: " + radius + 
               "\nHeight: " + height + 
               "\nSurface Area: " + surface_area() + 
               "\nVolume: " + volume() + "\n";
    }
}