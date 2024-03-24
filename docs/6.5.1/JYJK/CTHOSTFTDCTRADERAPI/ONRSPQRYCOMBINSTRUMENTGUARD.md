<p>请求查询组合合约安全系数响应，当执行ReqQryCombInstrumentGuard后，该方法被调用。</p>
<span class="anchor" id="6a827b5a-76f0-4704-ae15-ec1da576a021"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ab5a615b-6e08-48e0-8f74-fc0759e196f0"></span>
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
<span class="anchor" id="a25739a2-6ff1-4c0b-b3b7-0d45255b47c8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bf692c26-ff2a-4314-b531-73bceff92197"></span>
## 4.FAQ
<p>无</p>
