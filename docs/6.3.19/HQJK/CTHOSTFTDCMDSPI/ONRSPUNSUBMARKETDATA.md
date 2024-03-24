<p>取消订阅行情应答，当UnSubscribeMarketData后，调用此接口。</p>
<span class="anchor" id="7e66ee37-528c-441a-ab0d-a911c239415e"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6605a695-2b85-442c-9ce2-af1c6a1daf1f"></span>
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
<span class="anchor" id="33bc5fdf-5ad7-404a-ba0f-9e2f67544e90"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b2af863f-0538-4edf-b20b-599242f640a1"></span>
## 4.FAQ
<p>无</p>
