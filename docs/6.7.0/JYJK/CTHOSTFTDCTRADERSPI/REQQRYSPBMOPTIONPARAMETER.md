<p>请求SPBM期权合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMOPTIONPARAMETER/">OnRspQrySPBMOptionParameter</a></p>
<span class="anchor" id="fd4282d3-f76c-4764-8dfb-b34de238bdcb"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMOptionParameter(CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID) = 0;</p>
<span class="anchor" id="7f8097ba-0856-4f7a-a024-704a824dc9d1"></span>
## 2.参数
<p>pQrySPBMOptionParameter：SPBM期权合约保证金参数查询</p>
<pre><code>struct CThostFtdcQrySPBMOptionParameterField
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
<span class="anchor" id="7544b7fe-ada6-4bcf-8f26-f9d68795f144"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="bc22789e-bcb5-4bec-844c-42e3f417ddf6"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e787cdcb-3fb9-4504-97b8-e7e486c0f3b3"></span>
## 5.FAQ
<p>无</p>
