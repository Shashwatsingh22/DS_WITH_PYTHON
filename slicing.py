text = "X-DSPAM-Confidence:    0.8475";
pos=text.find("0");
val=text[pos:pos+6];
f=float(val);
print(f)