import numpy as np
import random as rd
import zipf

class  agent:
    zipf_dist = zipf.zipf(1, 500)
    def __init__(self, ID, _zipf_dist = zipf_dist):

        #TODO check zipf(1,500) np allow only a>1
        #self.q = max(np.random.zipf(range(2, 500)) * 10)
        self.q = _zipf_dist.sample() * 10
        #self.q = self.q[0]
        #self.q = 25
        self.c = rd.uniform(0.2, 1)*self.q
        self.p = rd.uniform(0.7, 1)
        self.ID = ID
        self.bid_in_SCE = self.c / self.q <= 0.5
        #self.q = self.q * self.p

    def introduce_self(self):
        print('agent ID: ', self.ID, 'c:',self.c,'q:',self.q,'p:',self.p)

    def set_contract(self, contract):
        self.contract = contract

    def set_single_contract(self, single_contract):
        self.single_contract = single_contract

    def Fixed_cont_bid_on_contract(self):
        self.Fixed_cont_bids = []
        self.Fixed_cont_all_q = []
        for cont in self.contract:
            if self.q >= cont.l and self.q < cont.l + 10:
                self.Fixed_cont_l_of_selected_cont = cont.l
                self.Fixed_cont_f_of_selected_cont = cont.f
                Fixed_cont_Bid = (1 - self.p) * cont.f + self.c
                self.Fixed_cont_bids.append(Fixed_cont_Bid)
                self.Fixed_cont_all_q.append(self.q)

                # else:  #oded!
                #    self.Fixed_cont_bids.append(None)
                return
        # q is higer from all contects l
        Fixed_cont_highest_contract = self.contract[-1]
        self.Fixed_cont_l_of_selected_cont = Fixed_cont_highest_contract.l
        self.Fixed_cont_f_of_selected_cont = Fixed_cont_highest_contract.f
        Fixed_cont_Bid = (1 - self.p) * Fixed_cont_highest_contract.f + self.c
        # if Fixed_cont_Bid <= cont.l / 2:
        self.Fixed_cont_bids.append(Fixed_cont_Bid)
        self.Fixed_cont_all_q.append(self.q)



        #print(self.bids)
        #print('Fixed_cont- The sum all of the q is: ', sum(self.all_q), 'KWh')

    def SCE_cont_bid_on_contract(self):
        for cont in self.contract:
            if self.q >= cont.l and self.q < cont.l + 10:
                self.SCE_cont_l_of_selected_cont = cont.l
                return
        SCE_cont_highest_contract = self.contract[-1]
        self.SCE_cont_l_of_selected_cont = SCE_cont_highest_contract.l


    def cliff_cont_bid_on_contract(self):
        self.Cliff_cont_bids = []
        self.Cliff_cont_all_q = []
        for cont in self.contract:
            if self.q >= cont.l and self.q < cont.l+10:
                self.Cliff_cont_l_of_selected_cont = cont.l
                self.Cliff_cont_f_of_selected_cont = cont.f
                Cliff_cont_Bid = (1 - self.p) * cont.f + self.c
                #if self.q < cont.alfa * cont.l:
                #    Cliff_cont_Bid = (1 - self.p) * cont.f + self.c
                #if self.q >= cont.alfa * cont.l and self.q < cont.l:
                #    Cliff_cont_Bid = (cont.l - self.q) * cont.beita + self.c
                #if self.q >= cont.l:
                #    Cliff_cont_Bid = 0 + self.c
                if Cliff_cont_Bid <= cont.l/2:
                    self.Cliff_cont_bids.append((Cliff_cont_Bid))
                    self.Cliff_cont_all_q.append((self.q))
                    return
                else:
                    self.Cliff_cont_bids.append(None)
                    return
        Cliff_cont_highest_contract = self.contract[-1]
        self.Cliff_cont_l_of_selected_cont = Cliff_cont_highest_contract.l
        self.Cliff_cont_f_of_selected_cont = Cliff_cont_highest_contract.f
        #if self.q < Cliff_cont_highest_contract.alfa * Cliff_cont_highest_contract.l:
        Cliff_cont_Bid = (1 - self.p) * Cliff_cont_highest_contract.f + self.c
        #if self.q >= Cliff_cont_highest_contract.alfa * Cliff_cont_highest_contract.l and self.q < Cliff_cont_highest_contract.l:
        #    Cliff_cont_Bid = (Cliff_cont_highest_contract.l - self.q) * Cliff_cont_highest_contract.beita + self.c
        #if self.q >= Cliff_cont_highest_contract.l:
        #    Cliff_cont_Bid = 0 + self.c
        if Cliff_cont_Bid <= Cliff_cont_highest_contract.l / 2:
            self.Cliff_cont_bids.append((Cliff_cont_Bid))
            self.Cliff_cont_all_q.append((self.q))
            return
        else:
            self.Cliff_cont_bids.append(None)
            return

    def Fixed_single_cont_bid_on_contract(self):
        self.Fixed_single_cont_bids = []
        self.Fixed_single_cont_all_q = []
        for cont in self.single_contract:
            if self.q >= cont.l:
                self.Fixed_single_cont_l_of_selected_cont = cont.l
                self.Fixed_single_cont_f_of_selected_cont = cont.f
                Fixed_single_cont_Bid = (1 - self.p) * cont.f + self.c
                #if Fixed_single_cont_Bid <= cont.l/2:
                self.Fixed_single_cont_bids.append(Fixed_single_cont_Bid)
                self.Fixed_single_cont_all_q.append(self.q)
                #    return
                #else:
                #    self.Fixed_single_cont_bids.append(None)
                #    return
            else:
                self.Fixed_single_cont_bids.append(None)
                return











