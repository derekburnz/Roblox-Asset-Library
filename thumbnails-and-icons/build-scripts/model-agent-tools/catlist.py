N = "Tabby,Tuxedo,Ginger,Snow,Brownie,Blue,Biscuit,Pepper,Butter,Moss,Acorn,Bramble,Fern,Torch".split(",")
print(",".join(f"CatCafe_Cat_{n}{s}" for n in N for s in ("", "_Sit", "_Work", "_Gold", "_Gold_Sit", "_Gold_Work")))
