from swaps_gateway import EthGoerliTestnetSwap

privkey = '21dd248b7b138c179ef8e07497be50d16e94614ca9bdd25af608deffe6b8aa6e'

swap_obj_eth_test = EthGoerliTestnetSwap(privkey)
swap_obj_eth_test.add_token("WETH", "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6", 18)
swap_obj_eth_test.add_token("WLTC", "0x343ce1626d4abD1839A8640a169a3740BfAA8754", 18)

# print("----------------------------")
print(swap_obj_eth_test.estimate_receiving_amount(0.001, "ETH", "WLTC"))
# print(swap_obj_eth_test.execute_swap_fixed_input(0.02, "ETH", "WLTC"))
print(swap_obj_eth_test.execute_swap_fixed_output(0.012, "ETH", "WLTC"))
