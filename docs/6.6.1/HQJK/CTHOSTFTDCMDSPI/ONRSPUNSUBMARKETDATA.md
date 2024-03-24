<p>取消订阅行情应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a>后，调用此接口。</p>
<span class="anchor" id="eb68fe1d-4353-426f-9bfe-bc56a16f4a65"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b2d5c5d7-7974-408d-a4bf-a7c6e9589a1c"></span>
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
<span class="anchor" id="d01c0ee8-25b5-4f23-867e-bb2e8f83fadc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="05e989b0-70eb-4ceb-9267-c23d7351a2e0"></span>
## 4.FAQ
<p>无</p>
