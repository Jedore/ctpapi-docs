<p>订阅行情应答，调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA/">SubscribeMarketData</a>后，通过此接口返回。</p>
<span class="anchor" id="0d1ceb1b-244e-4b43-a1c5-055789ae4a7f"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8617a479-874b-4173-b23e-15f3ef116404"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
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
<span class="anchor" id="b96b02b6-8833-49ab-a2db-e0f55df99787"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7970de32-bbc7-4e1c-8db8-37353b99b718"></span>
## 4.FAQ
<p>无</p>
