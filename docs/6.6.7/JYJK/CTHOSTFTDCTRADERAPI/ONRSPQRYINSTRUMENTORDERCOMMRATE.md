<p>请求查询报单手续费响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTORDERCOMMRATE/">ReqQryInstrumentOrderCommRate</a>后，该方法被调用。</p>
<span class="anchor" id="a8c79c03-302b-48cc-8ddc-71624d4d5454"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7b66e5d4-8d12-47a3-b626-4434381ab168"></span>
## 2.参数
<p>pInstrumentOrderCommRate：当前报单手续费的详细内容</p>
<pre><code>struct CThostFtdcInstrumentOrderCommRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///报单手续费
    TThostFtdcRatioType OrderCommByVolume;
    ///撤单手续费
    TThostFtdcRatioType OrderActionCommByVolume;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///报单手续费
    TThostFtdcRatioType OrderCommByTrade;
    ///撤单手续费
    TThostFtdcRatioType OrderActionCommByTrade;
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
<span class="anchor" id="23eddb27-a65c-4ad6-a5d2-c5ea824285ec"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c3c3e521-5b3c-4c3f-b245-d3a368dc10a3"></span>
## 4.FAQ
<p>无</p>
