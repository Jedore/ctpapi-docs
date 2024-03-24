<p>请求查询期权交易成本响应，当执行ReqQryOptionInstrTradeCost后，该方法被调用。</p>
<span class="anchor" id="8a88b802-8f23-412c-a06e-0647c1264f9b"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3ff4775f-184b-4d18-bac8-eedc33eb39f1"></span>
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
<span class="anchor" id="b7e5aad1-a513-484c-8ecb-ac277ece0b64"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a4d924c3-0b96-4d41-9c3f-4eb162987a1c"></span>
## 4.FAQ
<p>无</p>
