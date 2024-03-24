import json
from web3 import Web3
# from web3.exceptions import Web3Exception

# Conexión a Ganache
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Verificación de conexión
if not web3.is_connected():
    print("No se pudo conectar a Ganache. No olvides iniciarlo en segundo plano.")
    exit()

else:
    print("Conexion realizada.")
    
abi ='[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"_cliente","type":"address"}],"name":"alta_cliente","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_prestamista","type":"address"}],"name":"alta_prestamista","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"aprobar_prestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cliente","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositar_garantia","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"garantia","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrestamo","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidar_garantia","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"montoPrestamo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_cliente","type":"address"}],"name":"obtener_prestamos_por_prestatario","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prestamista","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prestamo","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prestamoAprobado","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reembolsar_prestamo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"_newPrestamo","type":"string"}],"name":"setPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_monto","type":"uint256"}],"name":"solicitar_prestamo","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

address = web3.to_checksum_address("0x7388d9a90d3ebca93cb4d360d94803799593c722")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.getPrestamo().call())
# Cuentas de prueba
owner_address = '0x71aB4f42A94C3999a3bEFda569a8C6914017b47E'
client_address = '0x0A36fa33751552E70A8d419945Ce32740e655054'

private_key = '0x67298bc9b18da47c382a3d5b4c526871e3b06c441b1d2bc470ee6d049c4e1963'

# Obtener el nonce actual de la cuenta
nonce = web3.eth.get_transaction_count(owner_address)

# Envío de la transferencia 1
tx = {
    'nonce': nonce,
    'to': client_address,
    'value': web3.to_wei(1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(1, 'gwei'),
}

# Incrementar el nonce para la segunda transacción
nonce += 1

# Envío de la transferencia 2
tx2 = {
    'nonce': nonce,
    'to': client_address,
    'value': web3.to_wei(15, 'ether'),
    'gas': 210000,
    'gasPrice': web3.to_wei(5, 'gwei'),
}

# Firmar el contrato
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
signed_tx2 = web3.eth.account.sign_transaction(tx2, private_key)

# Enviar la transacción
try:
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transacción realizada. \nNúmero de la transacción: ", web3.toHex(tx_hash))
except Exception as e:
    print("Error al enviar la transacción: ", e)

try:
    tx_hash2 = web3.eth.send_raw_transaction(signed_tx2.rawTransaction)
    print("Transacción realizada. \nNúmero de la transacción: ", web3.toHex(tx_hash2))
except Exception as e:
    print("Error al enviar la segunda transacción: ", e)

# Cargar el contrato
contract = web3.eth.contract(address=contract_address, abi=abi)

# Llamar a la función alta_prestamista
tx_hash = contract.functions.alta_prestamista().transact({'from': owner_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función alta_cliente
tx_hash = contract.functions.alta_cliente().transact({'from': owner_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función depositar_garantia
tx_hash = contract.functions.depositar_garantia().transact({'from': owner_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función solicitar_prestamo
tx_hash = contract.functions.solicitar_prestamo(lender_address, amount).transact({'from': client_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función aprobar_prestamo
tx_hash = contract.functions.aprobar_prestamo(borrower_address, loan_id).transact({'from': lender_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función reembolsar_prestamo
tx_hash = contract.functions.reembolsar_prestamo(loan_id).transact({'from': client_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función liquidar_garantia
tx_hash = contract.functions.liquidar_garantia(loan_id).transact({'from': client_address})
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Llamar a la función obtener_prestamos_por_prestatario
loans = contract.functions.obtener_prestamos_por_prestatario().call({'from': client_address})
print("Prestamos del cliente:", loans)

# Llamar a la función obtener_detalle_de_prestamo
loan_details = contract.functions.obtener_detalle_de_prestamo(loan_id).call({'from': client_address})
print("Detalles del préstamo:", loan_detail)

