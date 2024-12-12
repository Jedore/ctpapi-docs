<p>请求查询组合合约安全系数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a>后，该方法被调用。</p>
<span class="anchor" id="cff15c87-64d1-4e28-95d1-a06e45378e91"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="04328cf1-712e-48c1-8a4f-0d189b758040"></span>
## 2.参数
<p>pCombInstrumentGuard：组合合约安全系数</p>
<pre><code>struct CThostFtdcCombInstrumentGuardField
{
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///保留的无效字段
TThostFtdcOldInstrumentIDType   reserve1;
///比率类型
TThostFtdcRatioType GuarantRatio;
///交易所代码
TThostFtdcExchangeIDType    ExchangeID;
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
<span class="anchor" id="8a7421ff-4d9e-4051-9cba-94e29d6ce1f4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="68f6667e-e2dd-479c-bf0b-73f5bf5955ad"></span>
## 4.FAQ
<p>无</p>
