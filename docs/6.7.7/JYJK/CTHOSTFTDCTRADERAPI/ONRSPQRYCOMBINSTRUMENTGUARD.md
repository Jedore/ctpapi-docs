<p>请求查询组合合约安全系数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a>后，该方法被调用。</p>
<span class="anchor" id="fbd30b14-eb9d-4fc6-957b-0082a25fa91a"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="cf05b088-f803-4885-b0dc-553b5e633ab6"></span>
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
<span class="anchor" id="ae25136f-5896-40fa-8a4c-752bb09ad1b7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5b9beedd-19c9-4523-9222-c1826c59aac6"></span>
## 4.FAQ
<p>无</p>
