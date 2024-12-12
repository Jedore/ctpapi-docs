<p>订阅行情应答，调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA/">SubscribeMarketData</a>后，通过此接口返回。</p>
<span class="anchor" id="14ab4dad-fe26-44d3-8262-abd6f680ea50"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d7629191-f598-4608-8bae-5ae6a4645bde"></span>
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
<span class="anchor" id="dc938f23-dca9-4620-80e1-f5556cd4679d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3f8f66c0-62bc-428b-8493-a3b4ba493c73"></span>
## 4.FAQ
<p>无</p>
