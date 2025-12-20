/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package operadores;

import java.util.Scanner;

public class Operadores {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        double num1, num2, suma;
        System.out.println("Ingrese el primer número: ");
        num1 = teclado.nextDouble();
        System.out.println("Ingrese el segundo número: ");
        num2 = teclado.nextDouble();
        suma = num1 + num2;
        System.out.println("El resultado de la suma es: "+ suma);
    }
    
}
