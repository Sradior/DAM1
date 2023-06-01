
package proyectojava3;

public class ProyectoJava3 {

    public static void main(String[] args) {
        float operador1 = 4;
        float operador2 = 3;
        
        float suma = operador1 + operador2;
        System.out.println("la suma es " +suma);
        //para decimales
        float resta = operador1 - operador2;
        System.out.println("la suma es " +resta);
        
        float multi = operador1 * operador2;
        System.out.println("la multiplicación es " +multi);
        
        double division = operador1 / operador2;
        System.out.println("la división es " +division);
        //parte entera y decimal
        boolean igualdad = operador1 == operador2;
        System.out.println("la comparación es " +igualdad);
        //comparaciones
        boolean noigualdad = operador1 != operador2;
        System.out.println("la comparación es " +noigualdad);
        
        boolean menorq = operador1 < operador2;
        System.out.println("la comparación es " +menorq);
        
        boolean mayorq = operador1 > operador2;
        System.out.println("la comparación es " +mayorq);
    }
    
}
