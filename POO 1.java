public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private double quilometragem;

    // Construtor
    public Carro(String marca, String modelo, int ano, double quilometragem) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.quilometragem = quilometragem;
    }

    // Getters e Setters para marca, modelo e ano
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    // Getter para quilometragem
    public double getQuilometragem() {
        return quilometragem;
    }
}
