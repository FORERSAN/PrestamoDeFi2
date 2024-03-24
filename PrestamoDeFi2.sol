// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Prestamo {
    string public prestamo;
    address public prestamista;
    address public cliente;
    uint public garantia;
    uint public montoPrestamo;
    bool public prestamoAprobado;
    mapping(address => uint) public balances;

    constructor() {
        prestamo = "PrestamoDeFi";
    }

    function getPrestamo() public view returns (string memory) {
        return prestamo;
    }

    function setPrestamo(string memory _newPrestamo) public {
        prestamo = _newPrestamo;
    }

    function alta_prestamista(address _prestamista) public {
        prestamista = _prestamista;
    }

    function alta_cliente(address _cliente) public {
        cliente = _cliente;
    }

    function depositar_garantia() public payable {
        require(msg.sender == cliente, "Solo el cliente puede depositar la garantia.");
        garantia += msg.value;
        balances[msg.sender] += msg.value;
    }

    function solicitar_prestamo(uint _monto) public {
        require(msg.sender == cliente, "Solo el cliente puede solicitar un prestamo.");
        montoPrestamo = _monto;
    }

    function aprobar_prestamo() public {
        require(msg.sender == prestamista, "Solo el prestamista puede aprobar el prestamo.");
        require(montoPrestamo <= address(this).balance, "Fondos insuficientes en el contrato.");
        prestamoAprobado = true;
        //cliente.transfer(montoPrestamo);
    }

    function reembolsar_prestamo() public payable {
        require(msg.sender == cliente, "Solo el cliente puede reembolsar el prestamo.");
        require(prestamoAprobado, "El prestamo no ha sido aprobado.");
        require(msg.value == montoPrestamo, "El monto a reembolsar debe ser igual al monto del prestamo.");
       // prestamista.transfer(msg.value);
        prestamoAprobado = false;
    }

    function liquidar_garantia() public {
        require(msg.sender == prestamista, "Solo el prestamista puede liquidar la garantia.");
        require(!prestamoAprobado, "El prestamo aun esta activo.");
       // prestamista.transfer(garantia);
        garantia = 0;
    }

    // Esta función es un ejemplo y debe ser ajustada a tus necesidades.
    function obtener_prestamos_por_prestatario(address _cliente) public view returns (uint) {
        return balances[_cliente];
    }
}


//Cuenta principal   0x71aB4f42A94C3999a3bEFda569a8C6914017b47E
//Private Key  0x67298bc9b18da47c382a3d5b4c526871e3b06c441b1d2bc470ee6d049c4e1963
//Resultado prueba:Favorable:  [block:19 txIndex:-]from: 0x71a...7b47eto: Prestamo.(constructor)value: 0 weidata: 0x608...00033logs: 0hash: 0xb82...39730
//DireccionContrato - Address  0x7388d9a90d3ebca93cb4d360d94803799593c722
//ABI [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getPrestamo","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prestamo","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
