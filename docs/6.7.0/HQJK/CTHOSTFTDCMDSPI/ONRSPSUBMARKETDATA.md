<p>订阅行情应答，调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA/">SubscribeMarketData</a>后，通过此接口返回。</p>
<span class="anchor" id="960ff606-2c3a-4e51-b8ba-a13fa0f10d8e"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6b06b166-0259-48d5-b3f6-e4445fd7d74a"></span>
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
<span class="anchor" id="42cefeed-1fbb-40cd-bcc3-cc95dc71da62"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a037d942-fbb5-46ba-be1e-964c05b1aa66"></span>
## 4.FAQ
<p>无</p>
