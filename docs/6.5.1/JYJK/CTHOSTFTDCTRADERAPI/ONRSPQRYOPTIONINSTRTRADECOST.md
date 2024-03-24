<p>请求查询期权交易成本响应，当执行ReqQryOptionInstrTradeCost后，该方法被调用。</p>
<span class="anchor" id="9f156625-64c1-477d-a262-1361453eff4e"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="92c3b0b2-173f-4bdf-8ceb-ee48f3db8700"></span>
## 2.参数
<p>pOptionInstrTradeCost：期权交易成本</p>
<pre><code>struct CThostFtdcOptionInstrTradeCostField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
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
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="34726b16-867d-4377-9cb4-0022a199e862"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1fb09257-a26c-4d72-bcaf-e45c0468b8ae"></span>
## 4.FAQ
<p>无</p>
