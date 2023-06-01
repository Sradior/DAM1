

package proyectojava12;

public class ProyectoJava12 {

    public static void main(String[] args) {
        saludo("Oscar");
        saludo("Juan");
        saludo("Pablo");
        saludo();
        saludo("Julia","Miercoles");
    }
    
    public static void saludo(String nombre){
        System.out.println("Hola "+nombre+ ", que tal el dia?");
    }
    
    public static void saludo(){
        System.out.println("Hola , que tal el dia?");
    }
    
    public static void saludo(String nombre, String dia){
        System.out.println("Hola ,"+nombre+" que tal el dia?. Hoy es "+dia);
    }
    
    
}
