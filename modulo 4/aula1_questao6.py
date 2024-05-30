{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ca7f15f4-0bbc-4088-8823-7593a08ddc35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 10\n",
      " 5\n",
      " 5\n",
      " 2\n",
      " 6\n",
      " 656\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m cont \u001b[38;5;241m<\u001b[39m n:\n\u001b[0;32m      7\u001b[0m     quantia \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m())\n\u001b[1;32m----> 8\u001b[0m     tipo \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m()\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m tipo \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mS\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m     10\u001b[0m         soma_sapo \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m quantia\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1262\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1260\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1261\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1262\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_input_request(\n\u001b[0;32m   1263\u001b[0m     \u001b[38;5;28mstr\u001b[39m(prompt),\n\u001b[0;32m   1264\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parent_ident[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m   1265\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_parent(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1266\u001b[0m     password\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[0;32m   1267\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1305\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1302\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1303\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1304\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1305\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1306\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1307\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "n= int (input())\n",
    "cont = 0\n",
    "soma_sapo, soma_rato, soma_coelho= 0, 0, 0\n",
    "#interações\n",
    "\n",
    "while cont < n:\n",
    "    quantia = int(input())\n",
    "    tipo = input()\n",
    "    \n",
    "    if tipo == 'S':\n",
    "        soma_sapo += quantia\n",
    "    elif tipo == 'R':\n",
    "        soma_rato += quantia\n",
    "    elif tipo == \"C\":\n",
    "        soma_coelho += quantia\n",
    "\n",
    "cont += 1\n",
    "\n",
    "print(\"Total de cobaias:\", soma_sapo+soma_rato+soma_coelho)\n",
    "print(\"Total de sapos:\", soma_sapo)\n",
    "print(\"Total de ratos:\", soma_rato)\n",
    "print(\"Total de coelhos:\", soma_coelho)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d472fd3-37b9-4d71-9308-3471d278f107",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b891d44d-b5c6-4b0a-983a-4f15a413ec44",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
