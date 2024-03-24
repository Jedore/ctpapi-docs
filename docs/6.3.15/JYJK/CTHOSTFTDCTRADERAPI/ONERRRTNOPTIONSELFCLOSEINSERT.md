<p>期权自对冲录入错误回报，当执行ReqOptionSelfCloseInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="548d7ecc-512b-4f70-9911-97bfba823467"></span>
## 1.函数原型
<p>virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="ec11607f-e013-43e5-849c-726c9bc6fe2e"></span>
## 2.参数
<p>pInputOptionSelfClose：输入的期权自对冲</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///期权自对冲引用
    TThostFtdcOrderRefType OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///数量
    TThostFtdcVolumeType Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
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
<span class="anchor" id="e032a2b3-abd7-4128-a867-bb04b7592744"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e09d4c66-64e5-431c-bf93-192616b11979"></span>
## 4.FAQ
<p>无</p>
