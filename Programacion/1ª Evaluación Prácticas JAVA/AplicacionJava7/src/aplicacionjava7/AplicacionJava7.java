
package aplicacionjava7;

public class AplicacionJava7 {

    public static void main(String[] args) {
        int edad =35;
        
        if(edad<20){
            if(edad<10){
                System.out.println("Eres un niño");
            }else{
                System.out.println("Eres un adolescente");
            }
        }else{
            if(edad<30){
                System.out.println("Eres joven todavia pero no te despistas");
            }else{
                System.out.println("Ya no eres un chaval");
            }
            
        }
    }
           
}
