<p>订阅行情应答，调用SubscribeMarketData后，通过此接口返回。</p>
<span class="anchor" id="674c4f39-54f7-478c-b800-eda3b46d77a1"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6eedba90-85fb-414f-a3d5-3632dd6a35f8"></span>
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
<span class="anchor" id="006c81d2-3c0b-47d7-87d7-9b302a418998"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b0668e37-ca5f-4d56-81e5-1eb92e24fa4e"></span>
## 4.FAQ
<p>无</p>
