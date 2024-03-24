<p>请求SPBM期货合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a></p>
<span class="anchor" id="fe9774b6-a19d-48bf-b0b8-d9c67f67d51a"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMFutureParameter(CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID) = 0;</p>
<span class="anchor" id="6e89b7eb-c6a3-4143-98d3-378c49938969"></span>
## 2.参数
<p>pQrySPBMFutureParameter：SPBM期货合约保证金参数查询</p>
<pre><code>struct CThostFtdcQrySPBMFutureParameterField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d6260472-8944-4a6e-a0f0-c692994867d7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b4fcf1c4-c4ae-4c03-8da7-240fb3f5bf39"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6ffa75c5-a4d9-4198-a189-46b2dd28b787"></span>
## 5.FAQ
<p>无</p>
