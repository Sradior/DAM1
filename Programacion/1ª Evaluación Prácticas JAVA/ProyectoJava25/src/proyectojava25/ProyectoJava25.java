package proyectojava25;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class ProyectoJava25 {

    public static void main(String[] args) {
        Pattern patron = Pattern.compile("platano",Pattern.CASE_INSENSITIVE); //case_ es un modificador, puede ser misma pero redactada diferente
        Matcher frase = patron.matcher("El hombre construye robots"); //esto es dónde quiero buscarlo
    
        boolean encontrado = frase.find(); //boolean porque esto puede ser verdadero o falso
        
        if(encontrado){
            System.out.println("Si que se ha encontrado");
        }else{
            System.out.println("No que se ha encontrado");
        }
    }
    
    
}
