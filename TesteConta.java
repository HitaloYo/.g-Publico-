import java.util.Scanner;

public class TesteConta {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe os detalhes da conta:");
        System.out.print("Titular: ");
        String titular = scanner.nextLine();
        System.out.print("Número: ");
        int numero = scanner.nextInt();
        System.out.print("Agência: ");
        String agencia = scanner.next();
        System.out.print("Saldo: ");
        double saldo = scanner.nextDouble();
        System.out.print("Dia da abertura: ");
        int diaAbertura = scanner.nextInt();
        System.out.print("Mês da abertura: ");
        int mesAbertura = scanner.nextInt();
        System.out.print("Ano da abertura: ");
        int anoAbertura = scanner.nextInt();

        Conta minhaConta = new Conta(titular, numero, agencia, saldo, new Data());

        minhaConta.dataDeAbertura.preencherData(diaAbertura, mesAbertura, anoAbertura);

        System.out.println(minhaConta.getDadosConta());
    }
}


/*Conta minhaConta = new Conta("Fulano", 123, "001", 1000.0); // Criando uma instância da classe Conta
        Conta minhaConta2 = new Conta("Fulano", 456, "002", 1000.0);
        
        if (minhaConta == minhaConta2) { //Sempre será falso pois apesar de terem atributos iguais são objt diferentes
            System.out.println("iguais");
        } else {
            System.out.println("diferentes");
        }*/
