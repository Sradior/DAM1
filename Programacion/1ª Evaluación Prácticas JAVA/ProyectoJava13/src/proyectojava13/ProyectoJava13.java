package proyectojava13;

public class ProyectoJava13 {

    public static void main(String[] args) {
        Persona Manuel = new Persona();
        
        System.out.println("El nombre ahora de Manuel es:"+Manuel.nombre);
        Manuel.nombre = "Manuel";
        Manuel.edad = 35;
        System.out.println("El nombre ahora de Manuel es:"+Manuel.nombre);
        System.out.println("La edad ahora de Manuel es:"+Manuel.edad);
    }
    
}//new crea una instancia de un objeto definido por el usuario 
