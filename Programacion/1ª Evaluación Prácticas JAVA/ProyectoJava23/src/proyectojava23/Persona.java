
package proyectojava23;

public class Persona {
    double minx = 0;
        double maxx = 1920;
        double randomx = minx + Math.random() * (maxx - minx);
    public double x = randomx;
    
    double miny = 0;
        double maxy = 1080;
        double randomy = miny + Math.random() * (maxy - miny);
    public double y = randomy;
    
    public float direccion = 0; 
    
    public void moverBola(){
        double min = -0.5;
        double max = 0.5;
        double random = min + Math.random() * (max - min);
        direccion += random;
        x += Math.cos(direccion);
        y += Math.sin(direccion); 
        if(x > 400){direccion += Math.PI;}
        if(x > 0){direccion += Math.PI;}
        if(y > 400){direccion += Math.PI;}
        if(y > 0){direccion += Math.PI;}
    }
    
}
