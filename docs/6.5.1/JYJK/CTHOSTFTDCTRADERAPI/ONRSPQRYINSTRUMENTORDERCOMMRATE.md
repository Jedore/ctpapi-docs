<p>请求查询报单手续费响应，当执行ReqQryInstrumentOrderCommRate后，该方法被调用。</p>
<span class="anchor" id="3ceb779a-e066-4327-8fff-44b897d0d02d"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="dbe97b20-bd23-450e-9b0a-9ccf8ff4fe63"></span>
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
<span class="anchor" id="d2767db2-b1eb-4741-9710-5aa76567ef57"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b40888f9-25d6-4d47-bd75-2847690720ba"></span>
## 4.FAQ
<p>无</p>
