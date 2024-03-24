<p>请求查询期权交易成本响应，当执行ReqQryOptionInstrTradeCost后，该方法被调用。</p>
<span class="anchor" id="23bfa380-0a6d-4af9-bd77-c107b9858b1d"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="147c0dcf-eb5f-4a3a-8249-679b33e461ce"></span>
## 2.参数
<p>pOptionInstrTradeCost：期权交易成本</p>
<pre><code>struct CThostFtdcOptionInstrTradeCostField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权合约保证金不变部分
    TThostFtdcMoneyType FixedMargin;
    ///期权合约最小保证金
    TThostFtdcMoneyType MiniMargin;
    ///期权合约权利金
    TThostFtdcMoneyType Royalty;
    ///交易所期权合约保证金不变部分
    TThostFtdcMoneyType ExchFixedMargin;
    ///交易所期权合约最小保证金
    TThostFtdcMoneyType ExchMiniMargin;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="0217cce7-c84c-49fa-b17a-7007a2d9ecd5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="678f8e02-7dce-4d08-a1ed-57d6591a7a80"></span>
## 4.FAQ
<p>无</p>
