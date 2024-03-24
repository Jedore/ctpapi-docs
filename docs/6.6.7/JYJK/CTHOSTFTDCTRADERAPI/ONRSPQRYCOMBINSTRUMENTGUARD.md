<p>请求查询组合合约安全系数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a>后，该方法被调用。</p>
<span class="anchor" id="47f0554f-2ced-4ffc-94b1-d8dc26014907"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5cda1b7b-0d4b-4e47-9ec6-a68c669b3e25"></span>
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
<span class="anchor" id="af7139a7-108e-4b01-b71c-002ec21644a6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1f78d8bb-7042-4584-9a61-3e4af686e7ee"></span>
## 4.FAQ
<p>无</p>
