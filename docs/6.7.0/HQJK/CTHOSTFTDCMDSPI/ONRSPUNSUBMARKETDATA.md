<p>取消订阅行情应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a>后，调用此接口。</p>
<span class="anchor" id="63485331-e63e-4130-9b89-38e8cd87ed85"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4cc97fcb-32f8-44c7-97ff-fdac76daaf6f"></span>
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
<span class="anchor" id="eaedb366-62a2-46a1-aede-d43612d649e2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8b3ea747-dee6-4f34-99c3-c50f912ce8af"></span>
## 4.FAQ
<p>无</p>
