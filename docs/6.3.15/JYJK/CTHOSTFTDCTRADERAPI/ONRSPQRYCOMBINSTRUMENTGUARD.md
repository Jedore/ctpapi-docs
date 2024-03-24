<p>请求查询组合合约安全系数响应，当执行ReqQryCombInstrumentGuard后，该方法被调用。</p>
<span class="anchor" id="6cb09c48-d3a8-4fce-ade7-e3fca78c3d28"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="067310cd-7b5b-4d87-b7b1-4917a94492ec"></span>
## 2.参数
<p>pCombInstrumentGuard：组合合约安全系数</p>
<pre><code>struct CThostFtdcCombInstrumentGuardField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///比率类型
    TThostFtdcRatioType GuarantRatio;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
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
<span class="anchor" id="b38839ca-df81-4262-bc1c-f7e6dcab2021"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="121a3aba-bb23-48ff-b870-5611c155f677"></span>
## 4.FAQ
<p>无</p>
