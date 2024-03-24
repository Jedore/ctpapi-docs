<p>请求查询组合合约安全系数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a>后，该方法被调用。</p>
<span class="anchor" id="f9982b44-9368-48a1-921d-60581a967d4b"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8a9e283d-86f2-43a5-a4cf-f5363d2fde56"></span>
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
<span class="anchor" id="3884ad66-0fea-4274-9f64-18707d1a6b9f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f57f5039-7192-4ba5-98ee-0678a8cecdc4"></span>
## 4.FAQ
<p>无</p>
