from swaps_gateway import BinanceSmartChainTestnetSwap

privkey = '21dd248b7b138c179ef8e07497be50d16e94614ca9bdd25af608deffe6b8aa6e'

swap_obj_bsc_test = BinanceSmartChainTestnetSwap(privkey, "BNB")
swap_obj_bsc_test.add_token("WBNB", "0xae13d989daC2f0dEbFf460aC112a837C89BAa7cd", 18)
swap_obj_bsc_test.add_token("TST", "0x958dcC4AFbDaEEE587D88AA9B04EbBf52A419d83", 18)

print(swap_obj_bsc_test.estimate_receiving_amount(1, "BNB", "TST"))
print(swap_obj_bsc_test.execute_swap_fixed_input(0.02, "BNB", "TST"))
# print(swap_obj_bsc_test.execute_swap_fixed_output(0.02, "TST", "BNB"))
print(swap_obj_bsc_test.get_allowance_list())
print(swap_obj_bsc_test.approve_swap_contract("TST", 200))

