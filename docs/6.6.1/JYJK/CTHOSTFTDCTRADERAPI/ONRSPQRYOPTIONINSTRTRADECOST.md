<p>请求查询期权交易成本响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRTRADECOST/">ReqQryOptionInstrTradeCost</a>后，该方法被调用。</p>
<span class="anchor" id="62a32742-12f5-46ed-a689-fe8f3df85f89"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="189f0bc9-1823-489c-9c3d-76267c76656b"></span>
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
<span class="anchor" id="ac0d6360-ed12-4c2c-a479-46deb8943a70"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8c917139-4a98-49a4-9e7c-7b3cfafa3a66"></span>
## 4.FAQ
<p>无</p>
