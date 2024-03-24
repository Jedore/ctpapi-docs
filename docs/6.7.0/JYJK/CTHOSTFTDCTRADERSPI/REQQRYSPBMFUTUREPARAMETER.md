<p>请求SPBM期货合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a></p>
<span class="anchor" id="255032b7-f9eb-43c8-b9a8-63b80f7c2b64"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMFutureParameter(CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID) = 0;</p>
<span class="anchor" id="7dc0def4-b9c5-40f1-aec6-e251c0a51702"></span>
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
<span class="anchor" id="a887b879-d363-410f-a02c-84555ba264d2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0fd4f3ef-7b58-4877-af93-242366af71fd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4284d1e4-d9dc-4d8a-814b-8b98c925c3ed"></span>
## 5.FAQ
<p>无</p>
