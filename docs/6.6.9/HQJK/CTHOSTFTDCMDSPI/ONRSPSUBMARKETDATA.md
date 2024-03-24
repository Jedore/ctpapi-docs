<p>订阅行情应答，调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA/">SubscribeMarketData</a>后，通过此接口返回。</p>
<span class="anchor" id="e832c9af-85cd-4508-86fd-2aa859f41ae1"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6470ecfb-e2aa-491d-b587-bf64bec88372"></span>
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
<span class="anchor" id="dd5b39d2-ed15-4969-a6fa-be56397ca725"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e8a2f077-d234-40c6-bf65-c5f0cd23eef4"></span>
## 4.FAQ
<p>无</p>
