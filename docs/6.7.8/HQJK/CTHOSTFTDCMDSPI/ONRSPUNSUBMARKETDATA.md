<p>取消订阅行情应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a>后，调用此接口。</p>
<span class="anchor" id="c192a3c0-d272-4d4b-9db0-1dd22b9176d4"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="289a7cdb-0a28-4fd8-9292-1adc36d4c7d5"></span>
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
<span class="anchor" id="4e4084ff-6577-4eb5-9357-e7850e2e31e7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b1a2b7a4-946b-46d0-9935-2a165bd81d41"></span>
## 4.FAQ
<p>无</p>
