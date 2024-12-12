<p>获取已连接的前置的信息。包含前置地址、查询流控参数、FTD流控参数。连接成功后，可获取正确的前置地址信息，登录成功后，可获取正确的前置查询流控和FTD流控信息。</p>
<span class="anchor" id="4830dbf9-555f-4624-a7a3-a000a41d257e"></span>
## 1.函数原型
<p>virtual void GetFrontInfo(CThostFtdcFrontInfoField* pFrontInfo) =0;</p>
<span class="anchor" id="77c72954-9726-4f5d-9838-715fe5039b51"></span>
## 2.参数
<p>pFrontInfo:前置信息</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcAddressType</td>
<td style="TEXT-ALIGN: left;">FrontAddr</td>
<td style="TEXT-ALIGN: left;">前置地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcQueryFreqType</td>
<td style="TEXT-ALIGN: left;">QryFreq</td>
<td style="TEXT-ALIGN: left;">查询流控</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcQueryFreqType</td>
<td style="TEXT-ALIGN: left;">FTDPkgFreq</td>
<td style="TEXT-ALIGN: left;">FTD流控</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<span class="anchor" id="2f7820c4-e210-4ac1-a4a3-1bcdb1b67610"></span>
## 3.返回
<p>返回一个前置信息。</p>
<span class="anchor" id="18d8efaa-9244-43f9-ae8f-14e4ff7b93f4"></span>
## 4.调用示例
<pre><code>CThostFtdcFrontInfoField g_chpFrontInfo = {};
pUserApi-&gt;GetFrontInfo(&amp;g_chpFrontInfo);
printf("%s\n",g_chpFrontInfo.FrontAddr);
printf("%d\n",g_chpFrontInfo.FTDPkgFreq);
printf("%d\n", g_chpFrontInfo.QryFreq);
</code></pre>
<span class="anchor" id="d797591e-4a49-4164-bbc8-3ec46b107369"></span>
## 5.FAQ
