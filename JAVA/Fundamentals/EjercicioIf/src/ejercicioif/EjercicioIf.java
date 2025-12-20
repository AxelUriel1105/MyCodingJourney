
package ejercicioif;

import java.util.Scanner;

public class EjercicioIf {

    public static void main(String[] args) {
        int edad;
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese su edad");
        edad = teclado.nextInt();
        if (edad > 18){
            System.out.println("Eres mayor de 18 ");
        }
        else {
            if (edad == 18){
                System.out.println("Tienes exactamente 18 años");
            }
            else{
                System.out.println("No puedes acceder porque eres menor de edad");    
            }
        }
    }
    
}
