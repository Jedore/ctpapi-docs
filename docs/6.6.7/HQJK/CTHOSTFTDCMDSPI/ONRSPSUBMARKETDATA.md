<p>订阅行情应答，调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA/">SubscribeMarketData</a>后，通过此接口返回。</p>
<span class="anchor" id="6fe9bee0-1175-4d44-be28-36f65f930221"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="86491fc8-c300-4b11-86d8-9c8c4a2bc8d4"></span>
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
<span class="anchor" id="dd95fb8f-1776-4792-b991-cb48d937901b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="69f96b11-0f63-4c6a-ba19-86b4406d2949"></span>
## 4.FAQ
<p>无</p>
