<p>期权自对冲录入错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="ac79129d-abed-462b-8839-4d67736435b1"></span>
## 1.函数原型
<p>virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="17063d14-bad1-46c4-aa45-465f3643c0f0"></span>
## 2.参数
<p>pInputOptionSelfClose：输入的期权自对冲</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///期权自对冲引用
    TThostFtdcOrderRefType  OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType  OptSelfCloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType    CurrencyID;
    ///交易编码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="992bda26-acfe-4afe-87a4-dab04cbb9a79"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f5b2db63-be6b-4358-9a7c-ffeceb8cf033"></span>
## 4.FAQ
<p>无</p>
