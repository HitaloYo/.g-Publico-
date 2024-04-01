import java.util.Scanner;
public class TestaConta{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número da conta: ");
        String numeroConta = scanner.nextLine();

        System.out.print("Digite o saldo inicial da conta: ");
        double saldoInicial = scanner.nextDouble();

        System.out.print("Digite a taxa de rendimento da conta (%): ");
        double taxaRendimento = scanner.nextDouble();

        Conta minhaConta = new Conta(numeroConta, saldoInicial, taxaRendimento);

        // Menu de interação com o usuário
        int opcao;
        do {
            System.out.println("\n### Menu ###");
            System.out.println("1. Sacar");
            System.out.println("2. Depositar");
            System.out.println("3. Calcular Rendimento");
            System.out.println("4. Mostrar Dados da Conta");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o valor a sacar: ");
                    double valorSaque = scanner.nextDouble();
                    minhaConta.saca(valorSaque);
                    break;
                case 2:
                    System.out.print("Digite o valor a depositar: ");
                    double valorDeposito = scanner.nextDouble();
                    minhaConta.deposita(valorDeposito);
                    break;
                case 3:
                    double rendimento = minhaConta.calculaRendimento();
                    System.out.println("Rendimento: R$" + rendimento);
                    break;
                case 4:
                    minhaConta.getDadosConta();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        } while (opcao != 0);

        scanner.close();
    }
}