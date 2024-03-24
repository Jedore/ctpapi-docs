<p>期权自对冲录入请求响应，当执行ReqOptionSelfCloseInsert后，该方法被调用</p>
<span class="anchor" id="88c8e888-baa8-440e-9183-9aba2b9702e2"></span>
## 1.函数原型
<p>virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, , bool bIsLast) {};</p>
<span class="anchor" id="8bb87a04-34bb-49ff-8037-0721db5be350"></span>
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
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="f48c11ad-4547-422b-86f2-a38268ec3a33"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c16ca9af-d69d-41bb-869e-2c5ea6d9b10d"></span>
## 4.FAQ
<p>无</p>
